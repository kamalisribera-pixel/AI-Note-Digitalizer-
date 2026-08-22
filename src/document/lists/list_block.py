class ListBlock:
    def __init__(
        self,
        list_type,
        items
    ):
        self.list_type = list_type
        self.items = items


    def __repr__(self):

        return (
            f"ListBlock("
            f"type='{self.list_type}', "
            f"items={self.items}"
            f")"
        )