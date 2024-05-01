#from rxconfig import config

import reflex as rx
from RecursosIT_ReflexHackt.webparts.navbar import navbar
from RecursosIT_ReflexHackt.webparts.languageslinks.languageslinks import languages
from RecursosIT_ReflexHackt.pages.index import index
from RecursosIT_ReflexHackt.pages.pythonweb import python
from RecursosIT_ReflexHackt.pages.jsweb import javascript
from RecursosIT_ReflexHackt.pages.csweb import csharp
from RecursosIT_ReflexHackt.pages.javaweb import java
from RecursosIT_ReflexHackt.pages.tsweb import typescript
from RecursosIT_ReflexHackt.pages.kotlinweb import kotlin
from RecursosIT_ReflexHackt.pages.swiftweb import swift
from RecursosIT_ReflexHackt.pages.goweb import go
from RecursosIT_ReflexHackt.pages.rustweb import rust
from RecursosIT_ReflexHackt.pages.phpweb import php
from RecursosIT_ReflexHackt.estilos.stilos import ESTILO


class State(rx.State):
    """The app state."""


app = rx.App(
    style= ESTILO
)
app.add_page(index)
app.add_page(python)
app.add_page(javascript)
app.add_page(csharp)
app.add_page(java)
app.add_page(typescript)
app.add_page(kotlin)
app.add_page(swift)
app.add_page(go)
app.add_page(rust)
app.add_page(php)
