import re

from .list_item import ListItem
from .list_block import ListBlock


class ListDetector:

    BULLET_PATTERN = re.compile(
        r"^(\•|\-|\*|\+)\s+(.*)"
    )

    NUMBER_PATTERN = re.compile(
        r"^(\d+[\.\)])\s+(.*)"
    )


    INDENT_STEP = 20


    def detect(self, lines):

        items = []

        list_type = None


        if not lines:
            return None


        base_x = self._get_base_x(lines)


        for line in lines:

            result = self._extract_item(
                line
            )

            if not result:
                continue


            marker, text = result


            if marker in ["•", "-", "*", "+"]:
                list_type = "bullet"

            else:
                list_type = "numbered"


            x_position = self._get_x_position(
                line
            )


            level = int(
                (x_position - base_x)
                /
                self.INDENT_STEP
            )


            items.append(
                ListItem(
                    text,
                    marker,
                    level
                )
            )


        if not items:
            return None


        return ListBlock(
            list_type,
            items
        )


    def _get_base_x(self, lines):

        positions = []

        for line in lines:

            if line.blocks:

                positions.append(
                    line.blocks[0].bounding_box[0]
                )


            if not positions:
                return 0

            return min(positions)



    def _get_x_position(self, line):

        if line.blocks:

            return line.blocks[0].bounding_box[0]


        return 0



    def _extract_item(self, line):

        text = line.text.strip()


        bullet = self.BULLET_PATTERN.match(text)

        if bullet:

            return (
                bullet.group(1),
                bullet.group(2)
            )


        number = self.NUMBER_PATTERN.match(text)

        if number:

            return (
                number.group(1),
                number.group(2)
            )


        return None