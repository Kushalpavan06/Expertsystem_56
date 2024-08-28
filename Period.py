from experta import *

# Define a Fact class for storing subject information
class Subject(Fact):
    """Fact class to store subject data"""
    pass

# Define the knowledge engine class
class DayKnowledgeEngine(KnowledgeEngine):

    @Rule(Subject(subjects={"DWDM", "OOSE", "CN", "ES", "TUTORIAL", "SC LAB(WT)", "SPORTS"}))
    def monday(self):
        print("The day is: Monday")

    @Rule(Subject(subjects={"SEMP LAB", "DWDM","OOSE","LIBRARY","OE","H/M"}))
    def tuesday(self):
        print("The day is: Tuesday")

    @Rule(Subject(subjects={"OOSE", "ES", "CN", "CN LAB","OE","H/M"}))
    def wednesday(self):
        print("The day is: Wednesday")

    @Rule(Subject(subjects={"ES", "DWDM", "CN","OE","TUTORIAL","STEM"}))
    def thursday(self):
        print("The day is: Thursday")

    @Rule(Subject(subjects={"OOSE", "CN","ES","OE","DWDM","SS LAB"}))
    def friday(self):
        print("The day is: Friday")

    @Rule(Subject(subjects={""}))
    def saturday(self):
        print("The day is: Saturday/Sunday")

    @Rule(NOT(Subject(subjects=W())), salience=-1)
    def no_match(self):
        print("No matching day found.")

def main():
    # Initialize the knowledge engine
    engine = DayKnowledgeEngine()

    # Reset the engine to prepare it for new data
    engine.reset()

    # Prompt the user for input subjects
    user_input = input("Enter the subjects for the day, separated by commas: ")

    # Convert the user input into a set of subjects
    input_subjects = set(subject.strip() for subject in user_input.split(','))

    # Debugging: Print input subjects
    print(f"Input subjects: {input_subjects}")

    # Declare the facts (input data) to the engine
    engine.declare(Subject(subjects=input_subjects))

    # Run the inference engine
    engine.run()

if __name__ == "__main__":
    main()
