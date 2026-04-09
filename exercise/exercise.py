import pandas
from fpdf import FPDF




class Articles:
    def __init__(self, article_id):
        self.article_id = article_id
        self.article_name = df.loc[df["id"] == article_id, "name"].squeeze()
        self.article_price = df.loc[df["id"] == article_id, "price"].squeeze()


class Receipt:
    def __init__(self, article):
        self.article = article

    def generate(self):
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_auto_page_break(auto=False, margin=0)

        pdf.add_page()
        pdf.set_font("Times", size=24, style='B')
        pdf.set_text_color(0,0,0)
        pdf.cell(w=0, h=10, text=f"Receipt #: {self.article.article_id}", ln=1)
        pdf.cell(w=0, h=15, text=f"Article Id: {self.article.article_name}", ln=1)
        pdf.cell(w=0, h=20, text=f"Price: {self.article.article_price}", ln=1)

        pdf.output("output.pdf")


df = pandas.read_csv("articles.csv", dtype={"id": str, "price":str})

print(df)
article_id = input("What do you want to buy? ")
article = Articles(article_id)
receipt = Receipt(article)
receipt.generate()