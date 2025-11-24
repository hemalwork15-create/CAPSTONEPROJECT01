Feature: Upload documents to EduDocs

  Scenario: Upload a new document successfully
    Given the FastAPI app is running
    When I upload a document with title "Linear Algebra Notes", category_id 1, uploader_id 1
    Then the response should indicate success
    And the document should exist in the document list
