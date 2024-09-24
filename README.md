# GPA_Calculator

```markdown
# CGPA Calculator

This is a simple CGPA (Cumulative Grade Point Average) calculator web application. Users can input their grades and credits for different subjects, and the application will calculate and display the CGPA.

## Features

- Select grades from a dropdown menu.
- Adjust credits using a counter.
- Dynamically add multiple subjects.
- Calculate CGPA based on the input grades and credits.
- Responsive and user-friendly interface.

## Technologies Used

- HTML
- CSS
- JavaScript
- Flask (for initial setup, not required for static site)
- GitHub Pages (for hosting the static site)

## Setup Instructions

### Running Locally with Flask

1. **Clone the repository**:
   ```sh
   git clone https://github.com/<your-username>/<repository-name>.git
   cd <repository-name>
   ```

2. **Install Flask**:
   ```sh
   pip install flask
   ```

3. **Run the Flask application**:
   ```sh
   python app.py
   ```

4. **Open your browser** and go to `http://127.0.0.1:5000/`.

### Hosting on GitHub Pages

1. **Convert to a Static Site**:
   - Move the calculation logic to JavaScript (as shown in the `index.html` example above).

2. **Push the updated files to GitHub**:
   ```sh
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

3. **Enable GitHub Pages**:
   - Go to the repository on GitHub.
   - Click on "Settings".
   - Scroll down to the "GitHub Pages" section.
   - Select the branch you want to use (usually `main` or `master`) and the folder (usually `/root`).
   - Save the settings.

Your site will be available at `https://<your-username>.github.io/<repository-name>/`.

## Usage

1. **Open the application** in your web browser.
2. **Enter the grades and credits** for each subject.
3. **Click "Add Subject"** to add more subjects.
4. **Click "Calculate CGPA"** to see your CGPA.

## License

This project is licensed under the MIT License.

## Acknowledgements

- Developed - &copy; Mush

Feel free to contribute to this project by submitting issues or pull requests.

```

Replace `<your-username>` and `<repository-name>` with your actual GitHub username and repository name. This `README.md` file provides a comprehensive guide to setting up and using the CGPA Calculator project. If you need any more details or further customization, let me know! 😊
