from jinja2 import Environment, FileSystemLoader
import yaml

loader = FileSystemLoader("templates")
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)
template = env.get_template("router-nat.j2")

with open("data/routers-nat.yml") as f:
    routers = yaml.safe_load(f)

for router in routers:
    router_conf = "config/" + router["management_ip"] + "-exercise-nat.txt"
    with open(router_conf, "w") as f:
        config_content = template.render(
            nat_interface=router["nat_interface"],
            inside_interfaces=router["inside_interfaces"],
            access_list=router["access_list"]
        )
        f.write(config_content.strip())

print("NAT configuration files have been generated.")
