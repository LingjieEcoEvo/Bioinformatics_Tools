library(castor)
library(ape)

filename <- "tmp/renamed_rerooted_test_input.treefile"
mytree <- ape::read.tree(filename)

RED <- date_tree_red(mytree, anchor_node = NULL)

redvalue<-RED$REDs
labels<-RED$tree$node.label

if (is.null(labels) || length(labels) < length(redvalue)) {
  labels <- c("INT_0", labels)   # 补充根节点标签
  redvalue <- c(0, redvalue)    # 补充根节点的 RED 值
} else if (is.na(labels[1]) || labels[1] == "") {
  labels[1] <- "INT_0"          # 如果根节点已有占位但无名称，修正为 "INT_0"
}
ape::write.tree(RED$tree, file='tmp/RED_renamed_rerooted_test_input.treefile')

value <- data.frame(Label = labels, RED = redvalue, stringsAsFactors = FALSE)
if (!"INT_0" %in% value$Label) {
  value <- rbind(data.frame(Label = "INT_0", RED = 0), value)  # 添加 INT_0 行
}

# 提取叶节点标签，并为其 RED 值设置为 1
leaf_labels <- mytree$tip.label
leaf_values <- data.frame(Label = leaf_labels, RED = 1, stringsAsFactors = FALSE)

value <- rbind(value, leaf_values)



write.table(value, file="tmp/RED.tsv",sep = "\t",row.names=FALSE,quote = FALSE)