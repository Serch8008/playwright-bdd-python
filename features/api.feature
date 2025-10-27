Feature: API pública

  Background:
    Given un api cliente con base "https://jsonplaceholder.typicode.com"

  Scenario: GET /posts devuelve lista de posts
    When hago GET a "/posts"
    Then el status code debe ser 200
    And el header "content-type" debe incluir "application/json"
    And el body debe ser una lista con al menos 1 elemento
    And el primer elemento debe tener las llaves "userId,id,title,body"

  Scenario: POST /posts crea un post
    When hago POST a "/posts" con json:
      """
      {"title": "foo", "body": "bar", "userId": 1}
      """
    Then el status code debe ser 201 o 200
    And el body debe tener la llave "id"
