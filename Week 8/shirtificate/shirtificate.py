from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.image("./shirtificate.png",10, 70, 190)
        self.set_font("helvetica", "", 50)
        self.cell(0, 52, "CS50 Shirtificate", align="C")
        self.ln(20)

def main():
    name = input("Name: ")
    design(name)


def design(s):
    pdf = PDF()
    pdf.add_page(orientation="portrait", format="a4")
    pdf.set_font("helvetica", size=30)
    pdf.set_text_color(255,255,255)
    pdf.cell(0,213, f"{s} took CS50", align="C")
    pdf.set_auto_page_break(auto=False)
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()