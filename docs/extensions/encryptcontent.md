title: Encrypt Content
password: 12345

Ist das [`mkdocs-encryptcontent-plugin`](https://github.com/unverbuggt/mkdocs-encryptcontent-plugin) installiert, in der `mkdocs.yaml` Datei aktiviert und konfiguriert,
dann wird über das <svg class="svg-1em"><use xlink:href="#encrypted" /></svg> Symbol neben einer Seite in der Navigation angeziegt, dass der Inhalt der Seite verschlüsselt ist.

```yaml
plugins:
    #...
    - encryptcontent:
        title_prefix: ''
        summary: 'Encrypted Test Page.'
        placeholder: '12345'
        decryption_failure_message: 'Wrong password, please enter "12345".'
        encryption_info_message: 'Please enter "12345".'
        input_class: 'w3-input'
        button_class: 'w3-button w3-theme-l1 w3-hover-theme'
        hljs: False
        arithmatex: False
        mermaid2: False
        remember_password: true
        session_storage: true
        encrypted_something:
          myNav: [div, id]
          myToc: [div, id]
          myTocButton: [div, id]
        search_index: 'dynamically' #dynamically
        password_button: True
        password_button_text: 'ENTER'
        selfhost: true
        selfhost_download: false
        reload_scripts:
          - '#theme'

    #...
```

Um eine Seite zu verschlüsseln muss nur der Wert `password` gesetzt werden.

```markdown
password: 12345
```