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


        # Final decision
        if score >= 5:
            block.block_type = "heading"
        else:
            block.block_type = "paragraph"


    return blocks