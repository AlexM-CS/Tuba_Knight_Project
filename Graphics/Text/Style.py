# Created: 11-21-2024
# Last updated: 12-11-2024

# Built-in packages:

# External packages:

# Internal packages:

class Style:
    """
    Description:
    The Style class affects how something gets displayed.

    Fields:
    str bg_color - the color of the background
    str color - the color of the text
    list[str] styles - styles for this text (italics, bold, etc.)
    """
    bg_color = None
    color = None
    styles = None

    def __init__(self, bg_color = "black", color = "white", styles = []):
        """ Initializes this Style object with the given attributes. """
        self.bg_color = bg_color
        self.color = color
        self.styles = styles

    def __repr__(self):
        """ Returns a stylized version of the string when used with Text. """
        thisStyle = ""
        for style in self.styles:
            thisStyle += f"{style}"
        return f"[{self.color} on {self.bg_color} {thisStyle}]"