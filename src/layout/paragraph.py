def reconstruct_paragraphs(blocks):

    paragraphs = []

    current = None


    for block in blocks:

        if block.block_type == "heading":

            paragraphs.append(block)
            current = None
            continue


        if current is None:

            current = block

        else:

            previous_bottom = current.bbox[3]

            current_top = block.bbox[1]

            distance = current_top - previous_bottom


            if distance < 30:

                current.text += " " + block.text

                current.bbox[2] = max(
                    current.bbox[2],
                    block.bbox[2]
                )

                current.bbox[3] = block.bbox[3]

            else:

                paragraphs.append(current)
                current = block


    if current:
        paragraphs.append(current)


    return paragraphs