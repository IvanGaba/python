from ariadne import ObjectType, QueryType, ggl, make_executable_schema
from ariadne.asgi import GraphQL
import requests

type_defs = ggl("""
    type Query {
        people: [Person!]!
    }
    type Person {
        GitHub_login: String
        github name: String
        repos: String
    }
""")
query = QueryType()
@query.field("people")
def resolve_people(*_):
    return[
        r = documentation_url("https://docs.github.com/rest/reference/users#get-a-user")
        r = documentation_url("https://docs.github.com/rest/reference/repos#list-repositories-for-a-user")
    ]
person = ObjectType("Person")

@person.field("login")
def resolve_person_fullname(person, *_):
    return "%s %s %s" % (person["login"], person["name"], person["repos"])

shema = make_executable_schema(type_defs, [query, person])

app = GraphQL(shema, debug=True)
    print(login, name, repos)
