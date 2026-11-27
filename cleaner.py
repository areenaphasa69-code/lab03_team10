def clean_text(text):
    """ลบช่องว่างส่วนเกินในข้อความ เช่น "  hello   first  year  " → "hello first year" """
    return " ".join(text.split())