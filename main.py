from singleton import OfficeConfig
from factory import EmployeeFactory
from observer import AnnouncementService, EmployeeObserver


config = OfficeConfig.get_instance()
factory = EmployeeFactory()
alice = factory.create_employee("Developer", "Alice")
bob = factory.create_employee("Manager", "Bob")

service = AnnouncementService()
service.subscribe(alice)
service.subscribe(bob)
service.announce(f"Fire drill at 3 PM. {config.company_name} {config.location}")
