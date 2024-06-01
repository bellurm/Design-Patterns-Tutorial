# ÖRNEK 1
from abc import ABC, abstractmethod

# Abstract Class
class DataProcessor(ABC):
    def process(self):
        self.read_data()
        self.process_data()
        self.save_data()
    
    @abstractmethod
    def read_data(self):
        pass
    
    @abstractmethod
    def process_data(self):
        pass
    
    @abstractmethod
    def save_data(self):
        pass

# Concrete Class for CSV
class CSVDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from CSV file.")
    
    def process_data(self):
        print("Processing data from CSV file.")
    
    def save_data(self):
        print("Saving processed data to CSV file.")

# Concrete Class for JSON
class JSONDataProcessor(DataProcessor):
    def read_data(self):
        print("Reading data from JSON file.")
    
    def process_data(self):
        print("Processing data from JSON file.")
    
    def save_data(self):
        print("Saving processed data to JSON file.")

# Kullanım
csv_processor = CSVDataProcessor()
csv_processor.process()
# Output:
# Reading data from CSV file.
# Processing data from CSV file.
# Saving processed data to CSV file.

json_processor = JSONDataProcessor()
json_processor.process()
# Output:
# Reading data from JSON file.
# Processing data from JSON file.
# Saving processed data to JSON file.

print("#"*70)

# ÖRNEK 2
from abc import ABC, abstractmethod

# Abstract Class
class ReportGenerator(ABC):
    def generate_report(self):
        self.collect_data()
        self.format_report()
        self.print_report()

    @abstractmethod
    def collect_data(self):
        pass

    @abstractmethod
    def format_report(self):
        pass

    @abstractmethod
    def print_report(self):
        pass

# Concrete Class for HTML Report
class HTMLReportGenerator(ReportGenerator):
    def collect_data(self):
        self.data = "HTML Report Data"
        print("Collecting data for HTML report.")

    def format_report(self):
        self.formatted_data = f"<html><body>{self.data}</body></html>"
        print("Formatting report as HTML.")

    def print_report(self):
        print(f"Printing HTML report:\n{self.formatted_data}")

# Concrete Class for PDF Report
class PDFReportGenerator(ReportGenerator):
    def collect_data(self):
        self.data = "PDF Report Data"
        print("Collecting data for PDF report.")

    def format_report(self):
        self.formatted_data = f"PDF({self.data})"
        print("Formatting report as PDF.")

    def print_report(self):
        print(f"Printing PDF report:\n{self.formatted_data}")

# Kullanım
html_report = HTMLReportGenerator()
html_report.generate_report()
# Output:
# Collecting data for HTML report.
# Formatting report as HTML.
# Printing HTML report:
# <html><body>HTML Report Data</body></html>

pdf_report = PDFReportGenerator()
pdf_report.generate_report()
# Output:
# Collecting data for PDF report.
# Formatting report as PDF.
# Printing PDF report:
# PDF(PDF Report Data)
