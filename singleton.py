# Singleton Pattern : OfficeConfig

class OfficeConfig:
    _instance = None
    company_name = "TechCorp"
    location = "Noida"

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = OfficeConfig()
        return cls._instance
