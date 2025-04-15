import os
import subprocess
from Methods import database as db

def create_pdf(messages):
    temp = """  """
    for message in messages:

        if message['sender'] == 'ai':
            content = message['content']
            temp += f"""<div style="background-color:powderblue;padding:20px;border-radius:20px;margin-top:10px""><h1>{content}</h1></div>"""
        else:
            content = message['content']
            temp += f"""<div style="background-color:yellowgreen;padding:20px;border-radius:20px;margin-top:10px;text-align:right"><h1>{content}</h1></div>"""

    html_content = f"""
    <!DOCTYPE html>
    <html>
    </head>
    <body>
        {temp}
    </body>
    </html>
    """

    with open("temp.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    subprocess.run([
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={os.path.abspath("output.pdf")  }",
        os.path.abspath("temp.html")
    ])

    os.remove("temp.html")
    print(os.path.abspath("output.pdf"))
    print("PDF saved as 'output.pdf'")


if __name__ == "__main__":
    create_pdf("")