def detect_headings(blocks):

    for block in blocks:

        score = 0

        # Size signal
        if block.height >= 35:
            score += 1

        # Short text signal
        if block.word_count <= 5:
            score += 1

        # Uppercase signal
        if block.uppercase_ratio >= 0.5:
            score += 1

        # Numbering signal
        if block.has_numbering:
            score += 1

        # Spacing signal
        if block.gap_above >= 20:
            score += 1

        if block.gap_below >= 20:
            score += 1

        # Center alignment signal
        if block.center_offset <= 30:
            score += 1

        # Width signal
        if block.width_ratio <= 0.5:
            score += 1


        strong_signal = (
            block.uppercase_ratio >= 0.5
            or block.has_numbering
            or block.center_offset <= 30
        )
        # Final decision
        if block.word_count > 8:
            block.block_type = "paragraph"
            block.heading_level = 0
            continue

        # Strong structural rules first
        if block.numbering_type == "chapter":
            block.block_type = "heading"
            block.heading_level = 1

        elif block.numbering_type == "decimal":
            block.block_type = "heading"
            block.heading_level = 3

        # Normal heading detection
        elif score >= 5 and strong_signal:

            block.block_type = "heading"

            if score >= 6:
                block.heading_level = 2
            else:
                block.heading_level = 3

        # Paragraph
        else:
            block.block_type = "paragraph"
            block.heading_level = 0


    return blocks