repo_list_multi_page_1 = """
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
                  "name": "old-branch"
                },
                "branchProtectionRules": {
                  "edges": [
                    {
                      "node": {
                        "matchingRefs": {
                          "totalCount": 1,
                          "nodes": [
                            {
                              "name": "old-branch"
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
                "ref": {
                  "name": "old-branch"
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
                  "name": "old-branch"
                },
                "branchProtectionRules": {
                  "edges": [
                    {
                      "node": {
                        "matchingRefs": {
                          "totalCount": 1,
                          "nodes": [
                            {
                              "name": "old-branch"
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
                "ref": {
                  "name": "old-branch"
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
                  "name": "old-branch"
                },
                "branchProtectionRules": {
                  "edges": [
                    {
                      "node": {
                        "matchingRefs": {
                          "totalCount": 1,
                          "nodes": [
                            {
                              "name": "old-branch"
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
                "ref": {
                  "name": "old-branch"
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
repo_list_multi_page_2 = """
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
                  "ref": null
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
                  "ref": null
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
                    "name": "old-branch"
                  },
                  "branchProtectionRules": {
                    "edges": [
                      {
                        "node": {
                          "matchingRefs": {
                            "totalCount": 1,
                            "nodes": [
                              {
                                "name": "old-branch"
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
                  "ref": {
                    "name": "old-branch"
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
                  "ref": null
                }
              }
            ]
          }
        }
      }
    }
  }
"""

team_name_list_single_page = """
{
    "data": {
      "rateLimit": {
        "limit": 5000,
        "cost": 1,
        "remaining": 4989,
        "resetAt": "2021-06-18T13:41:33Z"
      },
      "organization": {
        "name": "My Org",
        "teams": {
          "totalCount": 223,
          "pageInfo": {
            "hasNextPage": false,
            "endCursor": ""
          },
          "nodes": [
            {
              "slug": "my-team"
            },
            {
              "slug": "my-admin-team"
            },
            {
              "slug": "justice-league"
            }
          ]
        }
      }
    }
  }
"""
team_name_list_multi_page_1="""
{
    "data": {
      "rateLimit": {
        "limit": 5000,
        "cost": 1,
        "remaining": 4989,
        "resetAt": "2021-06-18T13:41:33Z"
      },
      "organization": {
        "name": "My Org",
        "teams": {
          "totalCount": 223,
          "pageInfo": {
            "hasNextPage": true,
            "endCursor": "fd3kle2jkKLfdsklswHTjk=="
          },
          "nodes": [
            {
              "slug": "my-team"
            },
            {
              "slug": "my-admin-team"
            },
            {
              "slug": "justice-league"
            }
          ]
        }
      }
    }
  }
"""
team_name_list_multi_page_2 = """
{
    "data": {
      "rateLimit": {
        "limit": 5000,
        "cost": 1,
        "remaining": 4989,
        "resetAt": "2021-06-18T13:41:33Z"
      },
      "organization": {
        "name": "my-org",
        "teams": {
          "totalCount": 223,
          "pageInfo": {
            "hasNextPage": false,
            "endCursor": ""
          },
          "nodes": [
            {
              "slug": "my-additional-team"
            }
          ]
        }
      }
    }
  }
"""

team_repo_list_single_page = """
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
            "endCursor": "",
            "hasNextPage": false
          },
          "edges": [
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "name": "repo1"
              }
            },
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "name": "repo2"
              }
            },
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "name": "repo3"
              }
            }
          ]
        }
      }
    }
  }
}
"""
admin_team_repo_list_single_page = """
{
  "data": {
    "organization": {
      "id": "erhtjeKJHF4WjkhjkkEEbnncxerhtje=",
      "name": "my-org",
      "team": {
        "name": "my-admin-team",
        "repositories": {
          "totalCount": 111,
          "pageInfo": {
            "endCursor": "",
            "hasNextPage": false
          },
          "edges": [
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "name": "repo1"
              }
            },
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "name": "repo2"
              }
            },
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "name": "repo3"
              }
            },
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "name": "repo4"
              }
            }
          ]
        }
      }
    }
  }
}
"""
team_repo_list_multi_page_1 = """
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
                "name": "repo1"
              }
            },
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "name": "repo2"
              }
            },
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "name": "repo3"
              }
            }
          ]
        }
      }
    }
  }
}
"""
team_repo_list_multi_page_2 = """
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
            "endCursor": "",
            "hasNextPage": false
          },
          "edges": [
            {
              "permission": "WRITE",
              "node": {
                "isArchived": false,
                "name": "repo4"
              }
            }
          ]
        }
      }
    }
  }
}
"""
