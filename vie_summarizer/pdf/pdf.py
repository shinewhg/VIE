from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
# from reportlab.lib.units import inch
from vie_summarizer.rocketchat.message import Message

class PDF():
    def __init__(self):
        self.document = []
    
    def add_page_break(self):
        self.document.append(PageBreak())

    def add_thread_start(self):
        self.document.append(Paragraph('THREAD START', ParagraphStyle(name='Name', fontFamily='Arial', fontSize=12, alignment=TA_LEFT)))
        self.document.append(Spacer(1, 5))

    def add_thread(self, thread, base_url):
        for i, message in enumerate(thread.messages):
            self.add_message(message, message == thread.messages[0], base_url)

        self.document.append(Spacer(1, 10))

    def add_message(self, message: Message, top_level_post: bool, base_url: str):
        action = 'wrote' if top_level_post else 'replied'

        self.document.append(Paragraph(f'{message.user_name()} {action}:', ParagraphStyle(name='Name', fontFamily='Arial', fontSize=8, alignment=TA_LEFT)))

        images = message.images(base_url, 1500.0)

        for image in images or []:
            image_description = image.description
            if image_description is not None:
                self.document.append(Paragraph(f'{image_description}', ParagraphStyle(name='Name', fontFamily='Arial', fontSize=8, alignment=TA_LEFT)))

            self.document.append(Image(image.image_path, width=450, height=450, kind='proportional', lazy=2))

        msg = message.msg()
        if msg is not None:
            self.document.append(Paragraph(f'{message.msg()}', ParagraphStyle(name='Name', fontFamily='Arial', fontSize=8, alignment=TA_LEFT)))
    
        self.document.append(Spacer(1, 5))


    def add_thread_end(self):
        self.document.append(Paragraph('THREAD END', ParagraphStyle(name='Name', fontFamily='Arial', fontSize=14, alignment=TA_LEFT)))
        self.document.append(Spacer(1, 10))

    def generate_pdf(self, filename: str):
        SimpleDocTemplate(filename, pagesize=A4,
                   rightMargin=12, leftMargin=12,
                   topMargin=12, bottomMargin=6).build(self.document)
