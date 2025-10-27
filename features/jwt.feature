Feature: JWT HS256

  Scenario: Generar y validar token
    Given un payload con "sub"="sergio" y "role"="qa"
    When genero un token HS256 con expiracion de 60
    Then validar el token debe devolver "sergio"
