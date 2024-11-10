# LinkedIn Text Formatter

## Overview

The LinkedIn Text Formatter is a Streamlit-based web application that allows users to format their text with various Unicode styles.
Users can apply bold, italic, and strikethrough formatting to their text and then copy the formatted text for use on LinkedIn or other platforms.

## Features

- **Bold Formatting**: Convert text to bold Unicode characters.
- **Italic Formatting**: Convert text to italic Unicode characters.
- **Strikethrough Formatting**: Apply strikethrough effect to text.
- **Copy to Clipboard**: Easily copy the formatted text to the clipboard using a button.

## How to Use

1. **Enter Text**: Type or paste your text into the text area provided.
2. **Select Formatting Options**: Use the checkboxes to select the desired formatting options (Bold, Italic, Strikethrough).
3. **View Formatted Text**: The formatted text will be displayed in a separate text area.
4. **Copy Formatted Text**: Click the "Copy Text" button to copy the formatted text to your clipboard.

## Installation

1. Clone the repository:
    ```shell
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```shell
    cd <project-directory>
    ```
3. Install the required dependencies using pipenv:
    ```shell
    pipenv install
    ```

## Running the Application

To run the application, use the following command:

```shell
streamlit run app.py
```

There is also a run configuration provided in the repository for use with PyCharm:

![run-configuration](docs/images/run-configuration.png)