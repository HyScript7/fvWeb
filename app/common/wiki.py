class contentTable:
    def __init__(self, content: list):
        self.table = self.parse(content)
        self.simple = self.simpleParse(self.table)

    def parse(self, content: list) -> dict:
        """Returns the titles as a dict system

        Args:
            content (list): The Markdown content

        Returns:
            dict: {"# Heading 1": {"## Heading 2": {}, "## Another Heading 2": {"### Heading 3": {}}}}
        """
        titles = {}
        path = []
        for i in content:
            if not (i.startswith("#") and i.replace("#", "").startswith(" ")):
                continue
            # Modify path if necessary
            level = i.split(" ")[0].count("#")
            indentLevel = len(path)
            if indentLevel >= level:
                path = path[0 : level - 1]
                path.append(i)
            elif indentLevel < level:
                path.append(i)
            # Add path to corresponding title
            current = titles
            lp = path[0 : len(path) - 1]
            for y in lp:
                current = current[y]
            current[i] = {}
        return titles

    def simpleParse(self, table, prefix="") -> list:
        """Returns the titles as a list (in order)

        This is a recursive function

        Args:
            table (_type_): The dict system content table
            prefix (str, optional): What should every single titles be prefixed with? Defaults to "".

        Returns:
            list: The titles in order
        """
        titles = []
        for i, n in enumerate(table):
            p = f"{prefix}{i+1}"
            titles.append([p, n, n.replace("#", "").replace(" ", "", 1)])
            if len(table[n]):
                titles += self.simpleParse(table[n], prefix=(p + "."))
        return titles
