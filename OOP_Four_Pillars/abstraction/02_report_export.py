from abc import ABC, abstractmethod

class ReportExporter(ABC):
    @abstractmethod
    def export(self, title):
        pass

class PDFExporter(ReportExporter):
    def export(self, title):
        return f"Exporting {title} as PDF"

class CSVExporter(ReportExporter):
    def export(self, title):
        return f"Exporting {title} as CSV"

for exporter in [PDFExporter(), CSVExporter()]:
    print(exporter.export("Sales Report"))
