#%%

import difflib
import re

# ANSI escape colors
reset_ansi = "\x1b[0m"
color = {
    "equal": reset_ansi,
    "replace": "\x1b[1;33m",  # Bold yellow
    "insert": "\x1b[1;32m",  # Bold green
    "delete": "\x1b[1;31m",  # Bold red
}
color_space = {
    "replace": "\x1b[43m",  # Yellow
    "insert": "\x1b[42m",  # Green
    "delete": "\x1b[41m",  # Delete
}


def colorize(code: str, text: str) -> str:
    """Colorize strings based on difflib opcodes."""

    colored_text = ""
    if code in color_space.keys():
        splitted_text = list(filter(None, re.split(r"(\s+)", text)))
        for item in splitted_text:
            if item[0] == " ":
                colored_text += f"{color_space[code]}{item}"
            else:
                colored_text += f"{color[code]}{item}"
    else:
        colored_text = f"{color[code]}{text}"

    return colored_text


class SequenceMatcher(difflib.SequenceMatcher):
    """Extends difflib.SequenceMatcher class. Colorizes sequence differences."""

    colored_seq1 = ""
    colored_seq2 = ""

    def diff_strings(self, show_change_on_seq2=False):
        """Show colorized changes describing how to turn a into b."""

        self.colored_seq1 = ""
        self.colored_seq2 = ""
        for opcode, a0, a1, b0, b1 in self.get_opcodes():
            self.colored_seq2 += colorize(opcode, self.b[b0:b1])
            if opcode in ["insert"]:
                self.colored_seq1 += colorize(opcode, self.b[b0:b1])
            else:
                self.colored_seq1 += colorize(opcode, self.a[a0:a1])
                if opcode == "replace":
                    self.colored_seq1 += colorize("insert", self.b[b0:b1])

        # Reset color and style at the end of string to not affect terminal
        self.colored_seq1 += reset_ansi
        self.colored_seq2 += reset_ansi

        return self.colored_seq2 if show_change_on_seq2 else self.colored_seq1


def diff_strings(a, b, show_change_on_seq2=False):
    """Colorizes sequence differences. Show changes on seq1 on default."""
    s = SequenceMatcher(None, a, b, autojunk=False)
    return s.diff_strings(True) if show_change_on_seq2 else s.diff_strings(False)


#%%

# Class version
truth = """Lorem ipsum dolor sit amet,consectetur adipiscing elit,  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.f"""
predict = """Lorem furio dlfgor sit amet, consectetur apiscbgfing elit, sed do eiusmod tempor inciddfbunt ut labore et ddslore magna aliqua. Ut enim ad minim veniam, quis nostrud exercsfsation ullamco laboris assi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in volbcvbte velit esse cilldm doldsre eu fugiat nulla pafdgatur. Excepteur sint occaecat cupidatat non pident, sunt in culpa qui asafficia desert mollit anim id est lfdgarum."""
s = SequenceMatcher(None, predict, truth, autojunk=False)

print(s.diff_strings())
print(s.diff_strings(True))
print(s.ratio())

#%%

# Functional version
print(diff_strings(predict, truth))
print(diff_strings(predict, truth, show_change_on_seq2=True))
