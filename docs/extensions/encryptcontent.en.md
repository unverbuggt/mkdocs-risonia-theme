title: Encrypt content
password: 54321

If the [`mkdocs-encryptcontent-plugin`](https://github.com/unverbuggt/mkdocs-encryptcontent-plugin) is installed, activated in `mkdocs.yaml` and configured,
then encrypted pages are maked with the <svg class="svg-1em"><use xlink:href="#encrypted" /></svg> symbol at the navigation.

```yaml
plugins:
    #...
    - encryptcontent:
        title_prefix: ''
        summary: 'Verschlüsselte Testseite.'
        placeholder: '12345'
        password_button_text: 'ENTER'
        decryption_failure_message: 'Falsches Passwort, bitte "12345" eingeben.'
        encryption_info_message: 'Bitte "12345" eingeben.'
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
        selfhost: true
        selfhost_download: false
        reload_scripts:
          - '#theme'
        translations:
          en:
            title_prefix: ''
            summary: 'Encrypted Test Page.'
            placeholder: '54321'
            password_button_text: 'ENTER'
            decryption_failure_message: 'Wrong password, please enter "54321".'
            encryption_info_message: 'Please enter "54321".'
    #...
```

Pages can be marked for encryption by adding the meta `password`.

```markdown
password: 12345
```