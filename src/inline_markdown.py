from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type == TextType.TEXT:
            parts = node.text.split(delimiter)
            if len(parts) % 2 == 0:
                raise ValueError("Invalid markdown: delimiter not closed")
            for part in range(0, len(parts)):
                if parts[part] == "":
                    continue
                if part % 2 == 0:
                    new_node = TextNode(parts[part], TextType.TEXT)
                    new_nodes.append(new_node)
                else:
                    new_node = TextNode(parts[part], text_type)
                    new_nodes.append(new_node)
        else:
            new_nodes.append(node)
    return new_nodes


