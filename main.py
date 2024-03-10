import pygame
import speech_recognition as sr
import pywhatkit

def draw_AI(screen, font, text):
    bg = pygame.image.load("health.jpg")
    screen.fill((255, 255, 255))
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(bg, (0, 0))
    screen.blit(text_surface, (100, 100))
def draw_Person(screen, font, text):
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (100, 500)) 
# def draw_Response(screen, font, text):
#     text_surface = font.render(text, True, (0, 0, 0))
#     screen.blit(text_surface, (50, 600)) 
def command():
    recorder = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            audio = recorder.listen(source)
            text = recorder.recognize_google(audio)
            print(f"You said: {text}\n")
            return text.lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError as e:
            print(f"Error accessing Google Speech Recognition service: {e}")
            return ""
if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption("Health GPT Window")
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 36)
    results = ""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        text = command()
        if "goodbye" in text or "okay bye" in text or "turn off" in text or "quit" in text:
            print('See you later!')
            break
        # elif "search for" in text.lower():  
        #     pywhatkit.search(text)
        elif any(keyword in text for keyword in ["health", "rash", "medicine", 
            "pain", "sick", "feeling", "aches", "itch", "std", "throwup", "vomit" ,
            "puke" , "fungus" , "broken" , "gas" , "tore" , "tear""pain", "headache", 
            "fever", "nausea", "migraine", "inflammation", "muscle ache", "fatigue", 
            "dizziness", "symptom", "treatment", "prescription", "diagnosis", "medication", 
            "chronic", "acute", "disease", "condition", "therapy", "remedy", "doctor", 
            "nurse", "hospital", "pharmacy", "anatomy", "physiology", "prescription", 
            "aspirin", "ibuprofen", "acetaminophen", "analgesic", "antibiotic", 
            "anti-inflammatory", "vitamin", "mineral", "immune system", "consultation", 
            "x-ray", "MRI", "CT scan", "physical therapy", "alternative medicine", "holistic", "wellness","pain", "headache", "fever", "nausea", "migraine", "inflammation",
            "muscle ache", "fatigue", "dizziness", "symptom", "treatment",
            "prescription", "diagnosis", "medication", "chronic", "acute",
            "disease", "condition", "therapy", "remedy", "doctor", "nurse",
            "hospital", "pharmacy", "anatomy", "physiology", "aspirin",
            "ibuprofen", "acetaminophen", "analgesic", "antibiotic",
            "anti-inflammatory", "vitamin", "mineral", "immune system",
            "consultation", "x-ray", "MRI", "CT scan", "physical therapy",
            "alternative medicine", "holistic", "wellness", "allergy",
            "respiratory", "cardiology", "dermatology", "neurology",
            "gastroenterology", "orthopedics", "psychiatry", "pediatrics",
            "ophthalmology", "ophthalmologist", "gynecology", "obstetrics",
            "endocrinology", "urology", "oncology", "radiology", "laboratory",
            "blood pressure", "blood test", "vaccine", "immunization",
            "surgery", "anesthesia", "rehabilitation", "genetics", "geneticist",
            "infection", "virus", "bacteria", "immune response", "clinical trial",
            "emergency", "ambulance", "paramedic", "intensive care", "recovery",
            "pharmacist", "dosage", "side effects", "contraindication",
            "dose", "adverse reaction", "painkiller", "homeopathy", "nutrition",
            "exercise", "physical examination", "symptomatic", "genetic disorder",
            "disorder", "healthcare", "insurance", "patient", "medical history",
            "family history", "preventive care", "primary care", "specialist",
            "nutritionist", "obesity", "diabetes", "hypertension", "cholesterol",
            "stroke", "heart attack", "cancer", "Alzheimer's", "arthritis",
            "osteoporosis", "depression", "anxiety", "sleep disorder", "insomnia",
            "smoking cessation", "substance abuse", "addiction", "mental health",
            "counseling", "therapy", "palliative care", "hospice", "wheelchair",
            "crutches", "prosthesis", "braces", "hearing aid", "vision impairment",
            "dentist", "oral hygiene", "vaccination", "immunocompromised",
            "pharmacology", "pharmaceutical", "medication adherence", "over-the-counter",
            "prescription drug", "drug interaction", "clinical research",
            "health education", "screening", "diagnostic imaging", "laboratory test",
            "electrocardiogram", "ultrasound", "colonoscopy", "biopsy", "surgery",
            "rehabilitation", "physical therapy", "occupational therapy", "speech therapy",
            "disability", "genetic counseling", "pain management", "reproductive health",
            "contraception", "menopause", "fertility", "obstetrician", "gynecologist",
            "midwife", "ultrasound", "prenatal care", "postpartum", "breastfeeding",
            "childbirth", "infertility", "surrogacy", "fetal development", "pediatrician",
            "childhood immunization", "adolescent health", "puberty", "childhood obesity",
            "learning disability", "attention deficit hyperactivity disorder (ADHD)",
            "autism spectrum disorder", "down syndrome", "mental retardation",
            "cognitive impairment", "speech delay", "occupational therapy", "physical disability",
            "wheelchair", "hearing impairment", "visual impairment", "blindness",
            "deafness", "communication disorder", "speech-language pathologist",
            "audiologist", "speech therapy", "communication aids", "braille",
            "sign language", "assisted living", "long-term care", "nursing home",
            "hospice care", "respiratory therapy", "ventilator", "oxygen therapy",
            "rehabilitation", "physical therapist", "occupational therapist",
            "speech-language pathologist", "discharge planning", "continuum of care",
            "caregiver", "care coordination", "end-of-life care", "advance directive",
            "living will", "do not resuscitate (DNR)", "healthcare proxy", "hospice care",
            "palliative care", "bereavement", "grief counseling", "funeral",
            "cemetery", "cremation", "memorial service", "organ donation", "transplant",
            "coronary artery bypass grafting (CABG)", "angioplasty", "pacemaker",
            "heart valve replacement", "joint replacement", "arthroplasty", "hip replacement",
            "knee replacement", "organ transplant", "kidney transplant", "liver transplant",
            "lung transplant", "pancreas transplant", "bone marrow transplant", "organ rejection",
            "graft-versus-host disease (GVHD)", "reconstructive surgery", "plastic surgery",
            "cosmetic surgery", "dermatologic surgery", "oral and maxillofacial surgery",
            "ophthalmologic surgery", "orthopedic surgery", "urologic surgery", "vascular surgery",
            "anesthesia", "anesthesiologist", "general anesthesia", "local anesthesia",
            "spinal anesthesia", "epidural anesthesia", "conscious sedation", "post-anesthesia care",
            "adverse reaction", "anaphylaxis", "aspiration", "cardiac arrest", "hypotension",
            "hypoxia", "malignant hyperthermia", "nausea", "vomiting", "postoperative delirium",
            "surgical site infection", "wound healing", "scar", "hematoma", "thrombosis",
            "embolism", "deep vein thrombosis (DVT)", "pulmonary embolism (PE)",
            "postoperative pain", "analgesia", "pain scale", "patient-controlled analgesia (PCA)",
            "narcotic", "opioid", "tolerance", "dependence", "withdrawal", "addiction",
            "substance abuse", "rehabilitation", "physical therapy", "occupational therapy",
            "speech therapy", "psychological support", "counseling", "psychotherapy",
            "support groups", "mental health", "psychiatrist", "psychologist",
            "psychiatric medication", "antidepressant", "anxiolytic"]):  
            pywhatkit.search(text)
            
        screen.fill((255, 255, 255))
        draw_AI(screen, font, "We are your personal Health Search Engine, please say something related to health")
        draw_Person(screen, font, "Say Search for...(medical issue)")
        # draw_Response(screen, font, results)
        pygame.display.flip()
        clock.tick(30)
