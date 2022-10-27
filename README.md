# diffstrings

![License](https://img.shields.io/github/license/Uguudei/diffstrings)

Show difference of strings in color.

It extends difflib.SequenceMatcher class and provides a direct function too.

## Use

Example tests

```bash
# Truth text to compare with
truth = """Lorem ipsum dolor sit amet,consectetur adipiscing elit,  sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.f"""

# Supposedly wrong text to compare
predict = """Lorem furio dlfgor sit amet, consectetur apiscbgfing elit, sed do eiusmod tempor inciddfbunt ut labore et ddslore magna aliqua. Ut enim ad minim veniam, quis nostrud exercsfsation ullamco laboris assi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in volbcvbte velit esse cilldm doldsre eu fugiat nulla pafdgatur. Excepteur sint occaecat cupidatat non pident, sunt in culpa qui asafficia desert mollit anim id est lfdgarum."""
```

### Class

```bash
from diffstring import SequenceMatcher

s = SequenceMatcher(None, predict, truth, autojunk=False)
print(s.diff_strings())
print(s.diff_strings(True))
```

### Function

```bash
from diffstring import diff_strings

print(diff_strings(predict, truth))
print(diff_strings(predict, truth, show_change_on_seq2=True))
```
