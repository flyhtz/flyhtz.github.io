def generate_html(title, content):
    html_template = f'''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <link rel="stylesheet" href="../css/style.css">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
</head>
<body>
  <main>
    <div class="main-content">
      <nav class="navbar">
        <ul class="navbar-list">
          <li class="navbar-item">
            <a href="../../index.html" class="navbar-link">Go Back</a>
          </li>
        </ul>
      </nav>
      <article class="about active">
        <header>
          <h2 class="h2 article-title">{title}</h2>
        </header>
        <section class="about-text">
          {content}
        </section>
      </article>
    </div>
  </main>
  <script src="../js/script.js"></script>
  <script type="module" src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.esm.js"></script>
  <script nomodule src="https://unpkg.com/ionicons@5.5.2/dist/ionicons/ionicons.js"></script>
</body>
</html>
'''

    return html_template

def main():
    title = input("Enter the title of your blog: ")
    
    content = ""
    print("Enter your blog content. Type 'done' on a new line to finish.")
    while True:
        line = input()
        if line.strip().lower() == 'done':
            break
        content += f"<p>{line}</p>\n"
    
    html_content = generate_html(title, content)
    
    with open("output.html", "w") as f:
        f.write(html_content)
    
    print("HTML file generated as 'output.html'.")

if __name__ == "__main__":
    main()
