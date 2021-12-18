

class Attribute:

    def __init__(self, class_, values):
        self.class_ = class_
        self.values = values

    def __format_breakpoint(self, bp):
        sp = self.class_.split("-")
        return f"{sp[0]}-{bp}-{'-'.join(sp[1:])}"

    def generate_values(self):
        return "\n\t" + "\n\t".join(self.values) + "\n"

    def generate_breakpoint(self, bp):
        return f".{self.__format_breakpoint(bp)} {{{self.generate_values()}}}"

    def generate_raw(self):
        return f".{self.class_} {{{self.generate_values()}}}"


class Generator:

    def __init__(self, attributes, small_query, medium_query, large_query):
        self.attributes = attributes
        self.small_query = small_query
        self.medium_query = medium_query
        self.large_query = large_query

    def generate(self):
         return (
                 "\n\n".join([attribute.generate_raw() for attribute in self.attributes]) + 
                 f"\n\n\n{self.small_query}{{\n\n" + "\n\n".join([attribute.generate_breakpoint("sm") for attribute in self.attributes]) + "\n\n}" +
                 f"\n\n\n{self.medium_query}{{\n\n" + "\n\n".join([attribute.generate_breakpoint("md") for attribute in self.attributes]) + "\n\n}" +
                 f"\n\n\n{self.large_query}{{\n\n" + "\n\n".join([attribute.generate_breakpoint("lg") for attribute in self.attributes]) + "\n\n}"
                 )
         




ATTRIBUTES = [
        Attribute("d-flex", ["display: flex;"]),
        Attribute("d-grid", ["display: grid;"]),
        Attribute("d-none", ["display: none;"]),
        Attribute("d-block", ["display: block;"]),
        Attribute("flex-column", ["flex-direction: column;"]),
        Attribute("flex-row", ["flex-direction: row;"]),
        Attribute("flex-column-reverse", ["flex-direction: column-reverse;"]),
        Attribute("flex-row-reverse", ["flex-direction: row-reverse;"]),
        Attribute("flex-wrap", ["flex-wrap: wrap;"]),
        Attribute("gr-1", ["grid-row: 1"]),
        Attribute("gr-2", ["grid-row: 2"]),
        Attribute("gc-1", ["grid-column: 1"]),
        Attribute("gc-2", ["grid-column: 2"]),
        
        Attribute("position-absolute", ["position: absolute;"]),
        Attribute("position-relative", ["position: relative;"]),
        Attribute("position-fixed", ["position: fixed;"]),
        
        Attribute("m-auto", ["margin: auto;"]),
        Attribute("m-0", ["margin: 0em;"]),
        Attribute("m-05", ["margin: 0.5em;"]),
        Attribute("m-1", ["margin: 1em;"]),
        Attribute("m-2", ["margin: 2em"]),
        Attribute("m-3", ["margin: 4em;"]),
        Attribute("m-4", ["margin: 8em;"]),
        Attribute("m-5", ["margin: 16em;"]),
        Attribute("m-6", ["margin: 32em;"]),
        
        Attribute("ml-auto", ["margin-left: auto;"]),
        Attribute("ml-0", ["margin-left: 0;"]),
        Attribute("ml-05", ["margin-left: 0.5em;"]),
        Attribute("ml-1", ["margin-left: 1em;"]),
        Attribute("ml-2", ["margin-left: 2em;"]),
        Attribute("ml-3", ["margin-left: 4em;"]),
        Attribute("ml-4", ["margin-left: 8em;"]),
        Attribute("ml-5", ["margin-left: 16em;"]),
        Attribute("ml-6", ["margin-left: 32em;"]),
        
        Attribute("mr-auto", ["margin-right: auto;"]),
        Attribute("mr-0", ["margin-right: 0em;"]),
        Attribute("mr-05", ["margin-right: 0.5em;"]),
        Attribute("mr-1", ["margin-right: 1em;"]),
        Attribute("mr-2", ["margin-right: 2em;"]),
        Attribute("mr-3", ["margin-right: 4em;"]),
        Attribute("mr-4", ["margin-right: 8em;"]),
        Attribute("mr-5", ["margin-right: 16em;"]),
        Attribute("mr-6", ["margin-right: 32em;"]),
        
        Attribute("mt-auto", ["margin-top: auto;"]),
        Attribute("mt-0", ["margin-top: 0em;"]),
        Attribute("mt-05", ["margin-top: 0.5em;"]),
        Attribute("mt-1", ["margin-top: 1em;"]),
        Attribute("mt-2", ["margin-top: 2em;"]),
        Attribute("mt-3", ["margin-top: 4em;"]),
        Attribute("mt-4", ["margin-top: 8em;"]),
        Attribute("mt-5", ["margin-top: 16em;"]),
        Attribute("mt-6", ["margin-top: 32em;"]),
        
        Attribute("mb-auto", ["margin-bottom: auto;"]),
        Attribute("mb-0", ["margin-bottom: 0em;"]),
        Attribute("mb-05", ["margin-bottom: 0.5em;"]),
        Attribute("mb-1", ["margin-bottom: 1em;"]),
        Attribute("mb-2", ["margin-bottom: 2em;"]),
        Attribute("mb-3", ["margin-bottom: 4em;"]),
        Attribute("mb-4", ["margin-bottom: 8em;"]),
        Attribute("mb-5", ["margin-bottom: 16em;"]),
        Attribute("mb-6", ["margin-bottom: 32em;"]),
    
        Attribute("mh-auto", ["margin-right: auto;", "margin-left: auto;"]),
        Attribute("mh-0", ["margin-right: 0em;", "margin-left: 0em;"]),
        Attribute("mh-05", ["margin-right: 0.5em;", "margin-left: 0.5em"]),
        Attribute("mh-1", ["margin-right: 1em;", "margin-left: 1em;"]),
        Attribute("mh-2", ["margin-right: 2em;", "margin-left: 2em;"]),
        Attribute("mh-3", ["margin-right: 4em;", "margin-left: 4em;"]),
        Attribute("mh-4", ["margin-right: 8em;", "margin-left: 8em;"]),
        Attribute("mh-5", ["margin-right: 16em;", "margin-left: 16em;"]),
        Attribute("mh-6", ["margin-right: 32em;", "margin-left: 32em;"]),

        Attribute("mv-auto", ["margin-top: auto;", "margin-bottom: auto;"]),
        Attribute("mv-0", ["margin-top: 0em;", "margin-bottom: 0em;"]),
        Attribute("mv-05", ["margin-top: 0.5em;", "margin-bottom: 0.5em"]),
        Attribute("mv-1", ["margin-top: 1em;", "margin-bottom: 1em;"]),
        Attribute("mv-2", ["margin-top: 2em;", "margin-bottom: 2em;"]),
        Attribute("mv-3", ["margin-top: 4em;", "margin-bottom: 4em;"]),
        Attribute("mv-4", ["margin-top: 8em;", "margin-bottom: 8em;"]),
        Attribute("mv-5", ["margin-top: 16em;", "margin-bottom: 16em;"]),
        Attribute("mv-6", ["margin-top: 32em;", "margin-bottom: 32em;"]),

        Attribute("p-auto", ["padding: auto;"]),
        Attribute("p-0", ["padding: 0em;"]),
        Attribute("p-05", ["padding: 0.5em;"]),
        Attribute("p-1", ["padding: 1em;"]),
        Attribute("p-2", ["padding: 2em"]),
        Attribute("p-3", ["padding: 4em;"]),
        Attribute("p-4", ["padding: 8em;"]),
        Attribute("p-5", ["padding: 16em;"]),
        Attribute("p-6", ["padding: 32em;"]),
        
        Attribute("pl-auto", ["padding-left: auto;"]),
        Attribute("pl-0", ["padding-left: 0;"]),
        Attribute("pl-05", ["padding-left: 0.5em;"]),
        Attribute("pl-1", ["padding-left: 1em;"]),
        Attribute("pl-2", ["padding-left: 2em;"]),
        Attribute("pl-3", ["padding-left: 4em;"]),
        Attribute("pl-4", ["padding-left: 8em;"]),
        Attribute("pl-5", ["padding-left: 16em;"]),
        Attribute("pl-6", ["padding-left: 32em;"]),
        
        Attribute("pr-auto", ["padding-right: auto;"]),
        Attribute("pr-0", ["padding-right: 0em;"]),
        Attribute("pr-05", ["padding-right: 0.5em;"]),
        Attribute("pr-1", ["padding-right: 1em;"]),
        Attribute("pr-2", ["padding-right: 2em;"]),
        Attribute("pr-3", ["padding-right: 4em;"]),
        Attribute("pr-4", ["padding-right: 8em;"]),
        Attribute("pr-5", ["padding-right: 16em;"]),
        Attribute("pr-6", ["padding-right: 32em;"]),
        
        Attribute("pt-auto", ["padding-top: auto;"]),
        Attribute("pt-0", ["padding-top: 0em;"]),
        Attribute("pt-05", ["padding-top: 0.5em;"]),
        Attribute("pt-1", ["padding-top: 1em;"]),
        Attribute("pt-2", ["padding-top: 2em;"]),
        Attribute("pt-3", ["padding-top: 4em;"]),
        Attribute("pt-4", ["padding-top: 8em;"]),
        Attribute("pt-5", ["padding-top: 16em;"]),
        Attribute("pt-6", ["padding-top: 32em;"]),

        Attribute("pb-auto", ["padding-bottom: auto;"]),
        Attribute("pb-0", ["padding-bottom: 0em;"]),
        Attribute("pb-05", ["padding-bottom: 0.5em;"]),
        Attribute("pb-1", ["padding-bottom: 1em;"]),
        Attribute("pb-2", ["padding-bottom: 2em;"]),
        Attribute("pb-3", ["padding-bottom: 4em;"]),
        Attribute("pb-4", ["padding-bottom: 8em;"]),
        Attribute("pb-5", ["padding-bottom: 16em;"]),
        Attribute("pb-6", ["padding-bottom: 32em;"]),

        Attribute("ph-auto", ["padding-right: auto;", "padding-left: auto;"]),
        Attribute("ph-0", ["padding-right: 0em;", "padding-left: 0em;"]),
        Attribute("ph-05", ["padding-right: 0.5em;", "padding-left: 0.5em"]),
        Attribute("ph-1", ["padding-right: 1em;", "padding-left: 1em;"]),
        Attribute("ph-2", ["padding-right: 2em;", "padding-left: 2em;"]),
        Attribute("ph-3", ["padding-right: 4em;", "padding-left: 4em;"]),
        Attribute("ph-4", ["padding-right: 8em;", "padding-left: 8em;"]),
        Attribute("ph-5", ["padding-right: 16em;", "padding-left: 16em;"]),
        Attribute("ph-6", ["padding-right: 32em;", "padding-left: 32em;"]),

        Attribute("pv-auto", ["padding-top: auto;", "padding-bottom: auto;"]),
        Attribute("pv-0", ["padding-top: 0em;", "padding-bottom: 0em;"]),
        Attribute("pv-05", ["padding-top: 0.5em;", "padding-bottom: 0.5em"]),
        Attribute("pv-1", ["padding-top: 1em;", "padding-bottom: 1em;"]),
        Attribute("pv-2", ["padding-top: 2em;", "padding-bottom: 2em;"]),
        Attribute("pv-3", ["padding-top: 4em;", "padding-bottom: 4em;"]),
        Attribute("pv-4", ["padding-top: 8em;", "padding-bottom: 8em;"]),
        Attribute("pv-5", ["padding-top: 16em;", "padding-bottom: 16em;"]),
        Attribute("pv-6", ["padding-top: 32em;", "padding-bottom: 32em;"]),

        Attribute("w-0", ["width: 0;"]),
        Attribute("w-10", ["width: 10%;"]),
        Attribute("w-20", ["width: 20%;"]),
        Attribute("w-30", ["width: 30%;"]),
        Attribute("w-40", ["width: 40%;"]),
        Attribute("w-50", ["width: 50%;"]),
        Attribute("w-60", ["width: 60%;"]),
        Attribute("w-70", ["width: 70%;"]),
        Attribute("w-80", ["width: 80%;"]),
        Attribute("w-90", ["width: 90%;"]),
        Attribute("w-100", ["width: 100%;"]),

        Attribute("h-0", ["height: 0;"]),
        Attribute("h-10", ["height: 10%;"]),
        Attribute("h-20", ["height: 20%;"]),
        Attribute("h-30", ["height: 30%;"]),
        Attribute("h-40", ["height: 40%;"]),
        Attribute("h-50", ["height: 50%;"]),
        Attribute("h-60", ["height: 60%;"]),
        Attribute("h-70", ["height: 70%;"]),
        Attribute("h-80", ["height: 80%;"]),
        Attribute("h-90", ["height: 90%;"]),
        Attribute("h-100", ["height: 100%;"]),

        Attribute("vw-0", ["width: 0;"]),
        Attribute("vw-10", ["width: 10vw;"]),
        Attribute("vw-20", ["width: 20vw;"]),
        Attribute("vw-30", ["width: 30vw;"]),
        Attribute("vw-40", ["width: 40vw;"]),
        Attribute("vw-50", ["width: 50vw;"]),
        Attribute("vw-60", ["width: 60vw;"]),
        Attribute("vw-70", ["width: 70vw;"]),
        Attribute("vw-80", ["width: 80vw;"]),
        Attribute("vw-90", ["width: 90vw;"]),
        Attribute("vw-100", ["width: 100vw;"]),

        Attribute("vh-0", ["height: 0;"]),
        Attribute("vh-10", ["height: 10vh;"]),
        Attribute("vh-20", ["height: 20vh;"]),
        Attribute("vh-30", ["height: 30vh;"]),
        Attribute("vh-40", ["height: 40vh;"]),
        Attribute("vh-50", ["height: 50vh;"]),
        Attribute("vh-60", ["height: 60vh;"]),
        Attribute("vh-70", ["height: 70vh;"]),
        Attribute("vh-80", ["height: 80vh;"]),
        Attribute("vh-90", ["height: 90vh;"]),
        Attribute("vh-100", ["height: 100vh;"]),


        Attribute("fs-25", ["font-size: 25%;"]),
        Attribute("fs-50", ["font-size: 50%;"]),
        Attribute("fs-150", ["font-size: 150%;"]),
        Attribute("fs-200", ["font-size: 200%;"]),
        Attribute("fs-300", ["font-size: 300%;"]),
        Attribute("fs-400", ["font-size: 400%;"]),
        Attribute("fs-500", ["font-size: 500%;"]),
        Attribute("fs-600", ["font-size: 600%;"]),

        Attribute("lh-05", ["line-height: 0.5"]),
        Attribute("lh-10", ["line-height: 1"]),
        Attribute("lh-15", ["line-height: 1.5"]),
        Attribute("lh-20", ["line-height: 2"]),

        Attribute("border-radius-0", ["border-radius: 0;"]),
        Attribute("border-radius-1", ["border-radius: 1em;"]),
        Attribute("border-radius-2", ["border-radius: 2em;"]),
        Attribute("border-radius-3", ["border-radius: 4em;"]),
        Attribute("border-radius-4", ["border-radius: 8em;"]),
        Attribute("border-radius-5", ["border-radius: 16em;"]),

        Attribute("bg-dark", ["background-color: var(--color-dark);"]),
        Attribute("bg-light", ["background-color: var(--color-light);"]),
        Attribute("text-dark", ["color: var(--color-dark);"]),
        Attribute("text-light", ["color: var(--color-light);"]),
        Attribute("text-white", ["color: var(--color-white);"]),
        Attribute("text-center", ["text-align: center;"]),
        Attribute("text-left", ["text-align: left;"]),
        Attribute("text-right", ["text-align: right;"]),
        Attribute("overflow-visible", ["overflow: visible;"]),
        Attribute("overflow-clip", ["overflow: clip;"]),
        ]

if __name__ == "__main__":
    export = open("global.css", "w")
    print(Generator(ATTRIBUTES, "@media(max-width: 768px)", "@media(min-width: 769px) and (max-width: 1024px)", "@media(min-width: 1025px)").generate(), file=export)
