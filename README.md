# 💻 Refatoração de Código com Clean Code e Design Patterns

Este repositório contém a refatoração de um código utilizando os princípios do **Clean Code**, **SOLID**, e **Design Patterns**. A atividade foi desenvolvida para fins acadêmicos com o objetivo de demonstrar boas práticas, especialmente em legibilidade, manutenibilidade e testabilidade de código.

## 🎯 Objetivo da Atividade

Refatorar um código-fonte legado com más práticas de programação, tornando-o mais limpo, modular e orientado a objetos, sem alterar sua funcionalidade original. O trabalho visa:

- Aplicar os princípios do Clean Code.
- Utilizar Orientação a Objetos (OOP).
- Implementar pelo menos um Design Pattern.
- Escrever testes unitários para garantir a integridade funcional.
- Demonstrar versionamento via GitHub.

---

## 📂 Estrutura do Projeto

. ├── shapes.py # Código refatorado com OOP + Factory Pattern ├── test_shapes.py # └── README.md # Documentação do projeto


---

## ⚙️ Descrição da Refatoração

### 🔴 Código Original

```python
import math
def calcular_area(tipo, a, b=0):
    if tipo == 'quadrado':
        return a * a
    elif tipo == 'retangulo':
        return a * b
    elif tipo == 'circulo':
        return math.pi * a * a
    else:
        return None
```

❌ Problemas Identificados
Má prática: múltiplas responsabilidades em uma única função

Uso de magic strings

Nenhuma validação de tipo ou exceção

Nenhum teste automatizado

Nenhum uso de orientação a objetos

Nenhum padrão de projeto aplicado

✅ Melhorias Aplicadas
Criação de hierarquia de classes (Forma, Quadrado, Retangulo, Circulo)

Aplicação do Factory Pattern com FormaFactory

Introdução de exceções customizadas para controle de erro

Organização e nomenclatura seguindo Clean Code

Estrutura aberta para expansão sem modificação (Princípio Aberto/Fechado - SOLID)

Princípio/Padrão | Aplicação
OOP | Hierarquia de classes para representar formas
Factory Pattern | Criação de instâncias via fábrica centralizada (FormaFactory)
SOLID | Uso do Princípio Aberto/Fechado (OCP) e Responsabilidade Única (SRP)
DRY | Redução de duplicações através de abstrações
KISS | Lógica simples e clara, sem overengineering


📈 Versionamento
Este projeto está hospedado no GitHub com atualizações registradas nos meses de abril e maio, conforme exigido.

🧾 Conclusão
Refatorar códigos com base em princípios como Clean Code e SOLID não apenas melhora a legibilidade e organização, mas também reduz a chance de bugs, facilita a manutenção e permite maior escalabilidade.
Este projeto demonstra como técnicas simples de design podem tornar o código legado mais robusto, limpo e profissional.

