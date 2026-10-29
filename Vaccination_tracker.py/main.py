class Patient:
    total_patients = 0

    def __init__(self, patient_id, name, age, doses=0):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.doses = doses
        Patient.total_patients += 1

    def add_dose(self):
        self.doses += 1
        print(self.name, "received a vaccine dose.")

    def display_info(self):
        status = "Completed" if self.doses >= 2 else "Not completed"
        print(f"ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Doses: {self.doses}")
        print(f"Status: {status}")

    @classmethod
    def show_total_patients(cls):
        print(f"Total patients created: {cls.total_patients}")

    @staticmethod
    def valid_age(age):
        return age > 0 and age < 120

class VaccinationTracker:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"{patient.name} was added to the tracker.")

    def display_all(self):
        print("\n--- Vaccination Records ---")
        for patient in self.patients:
            patient.display_info()
            print()

    def find_patient(self, patient_id):
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        return None

tracker = VaccinationTracker()
patient1 = Patient("P001", "Mariama", 20, 1)
patient2 = Patient("P002", "Abdul", 22, 2)
tracker.add_patient(patient1)
tracker.add_patient(patient2)
patient1.add_dose()
tracker.display_all()
Patient.show_total_patients()

if Patient.valid_age(20):
    print("Age is valid.")
else:
    print("Age is not valid.")
