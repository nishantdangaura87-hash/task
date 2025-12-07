from datetime import datetime

attendance_records = [
    { "id": 1, "studentName": "John Doe", "rollNumber": "CS001", "class": "Class 10A", "date": "2025-12-01", "status": "present", "markedBy": "Admin" },
    { "id": 2, "studentName": "Jane Smith", "rollNumber": "CS002", "class": "Class 10A", "date": "2025-12-01", "status": "present", "markedBy": "Admin" },
    { "id": 3, "studentName": "Mike Johnson", "rollNumber": "CS003", "class": "Class 10A", "date": "2025-12-01", "status": "absent", "markedBy": "Admin" },
    { "id": 4, "studentName": "Sarah Williams", "rollNumber": "CS004", "class": "Class 10A", "date": "2025-12-01", "status": "present", "markedBy": "Admin" },
    { "id": 5, "studentName": "Tom Brown", "rollNumber": "CS005", "class": "Class 10A", "date": "2025-12-02", "status": "present", "markedBy": "Admin" },
    { "id": 6, "studentName": "Emily Davis", "rollNumber": "CS006", "class": "Class 10B", "date": "2025-12-02", "status": "present", "markedBy": "Admin" },
    { "id": 7, "studentName": "David Wilson", "rollNumber": "CS007", "class": "Class 10B", "date": "2025-12-02", "status": "absent", "markedBy": "Admin" },
    { "id": 8, "studentName": "Lisa Anderson", "rollNumber": "CS008", "class": "Class 10B", "date": "2025-12-02", "status": "present", "markedBy": "Admin" },
    { "id": 9, "studentName": "James Taylor", "rollNumber": "CS009", "class": "Class 10B", "date": "2025-12-03", "status": "present", "markedBy": "Admin" },
    { "id": 10, "studentName": "Mary Martinez", "rollNumber": "CS010", "class": "Class 10B", "date": "2025-12-03", "status": "absent", "markedBy": "Admin" },
]

# --- Filters ---
searchTerm = ""
filterStatus = "all"       # "all" | "present" | "absent"
filterClass = "all"         # "all" | "Class 10A" | "Class 10B"
startDate = ""              # "2025-12-01"
endDate = ""                # "2025-12-03"


def matches_date(date, start, end):
    if start and date < start:
        return False
    if end and date > end:
        return False
    return True


# --- Filtering Logic ---
filtered_records = []
for r in attendance_records:
    if searchTerm.lower() not in r["studentName"].lower() and \
       searchTerm.lower() not in r["rollNumber"].lower():
        continue

    if filterStatus != "all" and r["status"] != filterStatus:
        continue

    if filterClass != "all" and r["class"] != filterClass:
        continue

    if not matches_date(r["date"], startDate, endDate):
        continue

    filtered_records.append(r)


# --- Statistics ---
total = len(filtered_records)
present = sum(1 for r in filtered_records if r["status"] == "present")
absent = sum(1 for r in filtered_records if r["status"] == "absent")
attendance_rate = (present / total * 100) if total else 0


# --- Output ---
print("Filtered Records:")
for r in filtered_records:
    print(r)

print("\nStatistics:")
print("Total:", total)
print("Present:", present)
print("Absent:", absent)
print("Attendance Rate:", round(attendance_rate, 1), "%")
