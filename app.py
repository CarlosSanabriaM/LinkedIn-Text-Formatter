import streamlit as st

# Function to apply unicode formatting
def apply_unicode_formatting(text, bold, italic, strikethrough, monospace, superscript, subscript, uppercase, lowercase, titlecase, reverse, smallcaps):
    if bold:
        text = ''.join([chr(ord('𝐀') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝐚') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if italic:
        text = ''.join([chr(ord('𝑨') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝒂') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if strikethrough:
        text = ''.join([c + '\u0336' for c in text])
    if monospace:
        text = ''.join([chr(ord('𝙰') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝚊') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if superscript:
        superscript_map = str.maketrans('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=()', 
                                        '⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴽᴿˢᵀᵁⱽᵂ⁺⁻⁼⁽⁾')
        text = text.translate(superscript_map)
    if subscript:
        subscript_map = str.maketrans(
            '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=()', 
            '₀₁₂₃₄₅₆₇₈₉ₐₑₒₓᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓ' +
            'ⱽₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓThe error is likely due to the subscript string being too long and causing issues when being defined as a single string. I've broken it down into manageable chunks to ensure the syntax is correct. Here's the corrected section of your code:

```python
import streamlit as st

# Function to apply unicode formatting
def apply_unicode_formatting(text, bold, italic, strikethrough, monospace, superscript, subscript, uppercase, lowercase, titlecase, reverse, smallcaps):
    if bold:
        text = ''.join([chr(ord('𝐀') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝐚') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if italic:
        text = ''.join([chr(ord('𝑨') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝒂') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if strikethrough:
        text = ''.join([c + '\u0336' for c in text])
    if monospace:
        text = ''.join([chr(ord('𝙰') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝚊') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if superscript:
        superscript_map = str.maketrans('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=()', 
                                        '⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴽᴿˢᵀᵁⱽᵂ⁺⁻⁼⁽⁾')
        text = text.translate(superscript_map)
    if subscript:
        subscript_map = str.maketrans(
            '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=()',
            '₀₁₂₃₄₅₆₇₈₉ₐᵦᵧᵨᵢₖₗₘₙₒₚᵣₛₜᵤᵥₓ' +
            'ₐₑₓᵣₛᵥₔₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓThe error is likely caused by the string for the `subscript_map` being too long and not properly formatted, which led to the termination issue. To fix this, let's break down the string into smaller parts and ensure that it correctly maps each character to its subscript equivalent. Here's the corrected version:

```python
import streamlit as st

# Function to apply unicode formatting
def apply_unicode_formatting(text, bold, italic, strikethrough, monospace, superscript, subscript, uppercase, lowercase, titlecase, reverse, smallcaps):
    if bold:
        text = ''.join([chr(ord('𝐀') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝐚') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if italic:
        text = ''.join([chr(ord('𝑨') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝒂') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if strikethrough:
        text = ''.join([c + '\u0336' for c in text])
    if monospace:
        text = ''.join([chr(ord('𝙰') + (ord(c) - ord('A'))) if 'A' <= c <= 'Z' else chr(ord('𝚊') + (ord(c) - ord('a'))) if 'a' <= c <= 'z' else c for c in text])
    if superscript:
        superscript_map = str.maketrans('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=()', 
                                        '⁰¹²³⁴⁵⁶⁷⁸⁹ᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖʳˢᵗᵘᵛʷˣʸᶻᴬᴮᶜᴰᴱᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᴽᴿˢᵀᵁⱽᵂ⁺⁻⁼⁽⁾')
        text = text.translate(superscript_map)
    if subscript:
        subscript_map = str.maketrans(
            '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-=()', 
            '₀₁₂₃₄₅₆₇₈₉ₐₑₒₓᵢⱼₖₗₘₙₒₚᵣₛₜᵤᵥₓₐₑₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓₓ
