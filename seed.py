from app import create_app, db
from app.models import Category, Subcategory

app = create_app()

categories = [
    ("ID", "Identify", "Develop the organizational understanding to manage cybersecurity risk."),
    ("PR", "Protect", "Develop and implement appropriate safeguards to ensure delivery of critical services."),
    ("DE", "Detect", "Develop and implement appropriate activities to identify the occurrence of a cybersecurity event."),
    ("RS", "Respond", "Develop and implement appropriate activities to take action regarding a detected cybersecurity incident."),
    ("RC", "Recover", "Develop and implement appropriate activities to maintain plans for resilience and to restore capabilities or services."),
    ("GV", "Govern", "Establish and maintain a governance program to support the organization’s cybersecurity risk management.")
]

subcategories = [
    # Identify (ID)
    ("ID.AM-01", "Physical devices and systems within the organization are inventoried.", "ID"),
    ("ID.AM-02", "Software platforms and applications within the organization are inventoried.", "ID"),
    ("ID.AM-03", "Organizational communication and data flows are mapped.", "ID"),
    ("ID.AM-04", "External information systems are catalogued.", "ID"),
    ("ID.AM-05", "Resources are prioritized based on their classification, criticality, and business value.", "ID"),
    ("ID.AM-06", "Cybersecurity roles and responsibilities for the entire workforce and third-party stakeholders are established.", "ID"),

    # Protect (PR)
    ("PR.AC-01", "Identities and credentials are managed for authorized devices and users.", "PR"),
    ("PR.AC-02", "Physical access to assets is managed and protected.", "PR"),
    ("PR.AC-03", "Remote access is managed.", "PR"),
    ("PR.AC-04", "Access permissions are managed, incorporating the principles of least privilege and separation of duties.", "PR"),

    # Detect (DE)
    ("DE.CM-01", "The network is monitored to detect potential cybersecurity events.", "DE"),
    ("DE.CM-02", "The physical environment is monitored to detect potential cybersecurity events.", "DE"),
    ("DE.CM-03", "Personnel activity is monitored to detect potential cybersecurity events.", "DE"),

    # Respond (RS)
    ("RS.RP-01", "Response plans (Incident Response and Business Continuity) are executed during or after an incident.", "RS"),
    ("RS.CO-01", "Personnel know their roles and order of operations when a response is needed.", "RS"),
    ("RS.CO-02", "Incidents are reported consistent with established criteria.", "RS"),

    # Recover (RC)
    ("RC.RP-01", "Recovery plan is executed during or after a cybersecurity incident.", "RC"),
    ("RC.IM-01", "Recovery plans incorporate lessons learned.", "RC"),
    ("RC.IM-02", "Recovery strategies are updated.", "RC"),

    # Govern (GV)
    ("GV.RM-01", "Organizational risk management processes are established, managed, and agreed to by organizational stakeholders.", "GV"),
    ("GV.RM-02", "Organizational risk tolerance is determined and clearly expressed.", "GV"),
    ("GV.RM-03", "The organization’s determination of risk tolerance is informed by law, regulation, mission, and business requirements.", "GV")
]

with app.app_context():
    db.drop_all()
    db.create_all()

    for code, name, description in categories:
        cat = Category(code=code, name=name, description=description)
        db.session.add(cat)

    db.session.commit()

    for code, name, cat_code in subcategories:
        category = Category.query.filter_by(code=cat_code).first()
        if category:
            sub = Subcategory(code=code, name=name, category_id=category.id)
            db.session.add(sub)

    db.session.commit()
    print("Seed complete.")
