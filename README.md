
<p align="center">
  <img src="https://github.com/HexTide.png" width="100" alt="Hex Logo"/>
</p>

<h1 align="center">HexRoot</h1>
<p align="center"><strong>Foundation Layer of the HEX Ecosystem</strong></p>
<p align="center">
Events • Tasks • Bot Base Class
</p>
<p align="center">
Created by <a href="https://github.com/HexTide">HexTide</a>
</p>

---

## 🧠 What is HexRoot?

HexRoot is the foundational module for the HEX Automation Ecosystem.  
It provides the base classes and abstract definitions for all other bots and systems to build upon.

---

## 📁 Included Modules

| File             | Description |
|------------------|-------------|
| `base.py`        | Abstract BaseBot class |
| `event.py`       | Event object handler |
| `task.py`        | Task structure & executor logic |

---

## 🧪 Usage Example

```python
from hexroot.base import BaseBot

class MyBot(BaseBot):
    def start(self):
        print(f"Bot {self.name} started.")

MyBot("HexExample").start()
```

---

## 🔐 License

This module is licensed and bound to HEX system modules.  
It may only be used in official HEX bots.  
See LICENSE.txt for usage rules.

<p align="center">
  <strong>© HEX Automation • All Rights Reserved</strong><br/>
  Created by <a href="https://github.com/HexTide">HexTide</a>
</p>
