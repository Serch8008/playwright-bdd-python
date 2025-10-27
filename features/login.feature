Feature: Login funcional

  Scenario: Usuario accede correctamente con credenciales válidas
    Given que el usuario abre la página de inicio
    When ingresa las credenciales "standard_user" y "secret_sauce"
    Then debería ver la página de productos

  Scenario Outline: Usuario NO puede entrar con credenciales inválidas
    Given que el usuario abre la página de inicio
    When ingresa las credenciales "<user>" y "<password>"
    Then debería ver el mensaje de error "Epic sadface"

    Examples:
      | user            | password     |
      | locked_out_user | secret_sauce |
      | standard_user   | wrong_pass   |
