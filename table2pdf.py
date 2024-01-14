from fpdf import FPDF
import math

def generate_pdf(header, data):

    def fill_line_break(item, target_lines):
        current_lines = math.ceil(pdf.get_string_width(item) / col_width)
        len_diff = target_lines - current_lines
        prefix = "\n" * math.floor(len_diff / 2)
        suffix = "\n" * math.ceil(len_diff / 2)
        return f"{prefix}{item}\n{suffix}"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    col_width = pdf.w / 5.5
    row_height = pdf.font_size * 2.5
    y = pdf.get_y()

    combined_data = [header] + data
    for row in combined_data:
        x = pdf.get_x()
        longest_item = max(row, key=len)
        max_lines = math.ceil(pdf.get_string_width(longest_item) / col_width)
        updated_row = list(map(lambda x: fill_line_break(x, max_lines), row))
        for item in updated_row:
            pdf.multi_cell(col_width, row_height, txt=item, align="C", border=1)
            x += col_width
            pdf.set_xy(x, y)
        pdf.ln(row_height * max_lines)
        y += row_height * max_lines

    pdf.output("pdf_with_table.pdf")

if __name__ == "__main__":

    header = ["First name", "Last name", "Age", "City", "Life motto"]
    data = [
        ["Miu", "Kan", "33", "New York", "If you can't beat them, join them"],
        ["Mary", "Christmas", "49", "Helsinki", "What doesn't kill you makes you stranger"],
        ["Peter", "Peterson", "5", "Seoul", "How you doing"],
        ["Carriestheticalimetamorlodeminia", "Haha", "82", "Fez", "What you choose to focus on becomes your reality"]
    ]

    generate_pdf(header, data)