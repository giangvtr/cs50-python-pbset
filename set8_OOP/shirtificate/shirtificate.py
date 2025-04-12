from fpdf import FPDF

class shirt_w_title(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0,10, f"CS50 Shirtificate", align='C')

    def shirtificate(self,name):
        # Add shirt image
        self.image("shirtificate.png", x=0, y=60)

        #Add username
        self.ln(60)
        self.set_font("Arial", "B", 15)
        self.cell(0,10, f"{name} took cS50", align = 'C')

def main():
    name = input("Name: ").strip()
    pdf = shirt_w_title(orientation = "P", unit = "mm", format = "A4")
    pdf.add_page()
    pdf.header()
    pdf.shirtificate(name)

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()


