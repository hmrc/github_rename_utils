repo_with_64_branches = """
{
  "data": {
    "repository": {
      "refs": {
        "nodes": [
          {
            "name": "branch1"
          },
          {
            "name": "branch2"
          },
          {
            "name": "branch3"
          },
          {
            "name": "branch4"
          },
          {
            "name": "branch5"
          },
          {
            "name": "branch6"
          },
          {
            "name": "branch7"
          },
          {
            "name": "branch8"
          },
          {
            "name": "branch9"
          },
          {
            "name": "main"
          }
        ],
        "totalCount": 64
      }
    }
  }
}
"""

repo_list_page_1 = """
{
  "data": {
    "organization": {
      "id": "erhtjeKJHF4WjkhjkkEEbnncxerhtje=",
      "name": "my-org",
      "team": {
        "name": "my-team",
        "repositories": {
          "totalCount": 111,
          "pageInfo": {
            "endCursor": "fd3kle2jkKLfdsklswHTjk==",
            "hasNextPage": true
          },
          "edges": [
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "id": "fdFJKDSFJDSFDKLSjreldjs9c9dmsk=",
                "name": "repo1",
                "defaultBranchRef": {
                  "id": "fhddjksfhdfhdsfhhjew3RENCKCIDSHFHDdjksfhdfhd",
                  "name": "master"
                },
                "branchProtectionRules": {
                  "edges": [
                    {
                      "node": {
                        "matchingRefs": {
                          "totalCount": 1,
                          "nodes": [
                            {
                              "name": "master"
                            }
                          ]
                        },
                        "requiredStatusCheckContexts": [
                          "some-check-pr-builder"
                        ]
                      }
                    }
                  ]
                },
                "pullRequests": {
                  "totalCount": 8
                },
                "branches": {
                  "totalCount": 17
                }
              }
            },
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "id": "djklsfjkdfjdklsfjdklsjfksdlsfj=",
                "name": "repo2",
                "defaultBranchRef": {
                  "id": "fdjksfjdkfjdklsjfdklsjfkdlsfjkldsfjdksllfdff",
                  "name": "master"
                },
                "branchProtectionRules": {
                  "edges": [
                    {
                      "node": {
                        "matchingRefs": {
                          "totalCount": 1,
                          "nodes": [
                            {
                              "name": "master"
                            }
                          ]
                        },
                        "requiredStatusCheckContexts": []
                      }
                    }
                  ]
                },
                "pullRequests": {
                  "totalCount": 4
                },
                "branches": {
                  "totalCount": 34
                }
              }
            },
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "id": "djklsfjkdfjdklsfjdklsjfksdlsfj=",
                "name": "repo3",
                "defaultBranchRef": {
                  "id": "fdjksfjdkfjdklsjfdklsjfkdlsfjkldsfjdksllfdff",
                  "name": "master"
                },
                "branchProtectionRules": {
                  "edges": [
                    {
                      "node": {
                        "matchingRefs": {
                          "totalCount": 1,
                          "nodes": [
                            {
                              "name": "master"
                            }
                          ]
                        },
                        "requiredStatusCheckContexts": []
                      }
                    }
                  ]
                },
                "pullRequests": {
                  "totalCount": 4
                },
                "branches": {
                  "totalCount": 34
                }
              }
            }
          ]
        }
      }
    }
  }
}
"""

repo_list_page_2 = """
{
    "data": {
      "organization": {
        "id": "erhtjeKJHF4WjkhjkkEEbnncxerhtje=",
        "name": "my-org",
        "team": {
          "name": "my-team",
          "repositories": {
            "totalCount": 111,
            "pageInfo": {
              "endCursor": "Xd3kle2jkKLfdsklswHTjk==",
              "hasNextPage": false
            },
            "edges": [
              {
                "permission": "WRITE",
                "node": {
                  "isArchived": true,
                  "id": "fdhdjkshk6778T6HJGUf4wffdhsFkfh=",
                  "name": "repo-fhddjksfhk",
                  "defaultBranchRef": {
                    "id": "fdjksfjdkfjdklsjfdklsjfkdlsfjkldsfjdksllfdff",
                    "name": "main"
                  },
                  "branchProtectionRules": {
                    "edges": [
                      {
                        "node": {
                          "matchingRefs": {
                            "totalCount": 1,
                            "nodes": [
                              {
                                "name": "main"
                              }
                            ]
                          },
                          "requiredStatusCheckContexts": []
                        }
                      }
                    ]
                  },
                  "pullRequests": {
                    "totalCount": 0
                  },
                  "branches": {
                    "totalCount": 2
                  }
                }
              },
              {
                "permission": "WRITE",
                "node": {
                  "isArchived": false,
                  "id": "fdFJKDSFJDSFDKLSjreldjs9c9dmsk=",
                  "name": "repo-saderwkrhs",
                  "defaultBranchRef": {
                    "id": "fhddjksfhdfhdsfhhjew3RENCKCIDSHFHDdjksfhdf==",
                    "name": "main"
                  },
                  "branchProtectionRules": {
                    "edges": [
                      {
                        "node": {
                          "matchingRefs": {
                            "totalCount": 1,
                            "nodes": [
                              {
                                "name": "main"
                              }
                            ]
                          },
                          "requiredStatusCheckContexts": []
                        }
                      }
                    ]
                  },
                  "pullRequests": {
                    "totalCount": 0
                  },
                  "branches": {
                    "totalCount": 1
                  }
                }
              },
              {
                "permission": "READ",
                "node": {
                  "isArchived": false,
                  "id": "fdFJKDSFJDSFDKLSjreldjs9c9dmsk=",
                  "name": "repo-thjrecvix",
                  "defaultBranchRef": {
                    "id": "fhddjksfhdfhdsfhhjew3RENCKCIDSHFHDdjksfhdfhd",
                    "name": "master"
                  },
                  "branchProtectionRules": {
                    "edges": [
                      {
                        "node": {
                          "matchingRefs": {
                            "totalCount": 1,
                            "nodes": [
                              {
                                "name": "master"
                              }
                            ]
                          },
                          "requiredStatusCheckContexts": []
                        }
                      }
                    ]
                  },
                  "pullRequests": {
                    "totalCount": 0
                  },
                  "branches": {
                    "totalCount": 2
                  }
                }
              },
              {
                "permission": "WRITE",
                "node": {
                  "isArchived": false,
                  "id": "fd789DSHFsvcxjkfrketsancdsnjKfe=",
                  "name": "repo-fdhiob",
                  "defaultBranchRef": {
                    "id": "mkBF68fsdbk7LCFDBNFREbfd4bxsjkfBHFDJGFdrbk==",
                    "name": "main"
                  },
                  "branchProtectionRules": {
                    "edges": [
                      {
                        "node": {
                          "matchingRefs": {
                            "totalCount": 1,
                            "nodes": [
                              {
                                "name": "main"
                              }
                            ]
                          },
                          "requiredStatusCheckContexts": []
                        }
                      }
                    ]
                  },
                  "pullRequests": {
                    "totalCount": 0
                  },
                  "branches": {
                    "totalCount": 1
                  }
                }
              }
            ]
          }
        }
      }
    }
  }
"""