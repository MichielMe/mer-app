/// <reference path="../pb_data/types.d.ts" />
migrate((db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("xz7ejtfibmeoyom")

  collection.indexes = [
    "CREATE UNIQUE INDEX `idx_i0kL95B` ON `MERdata` (`material_id`)"
  ]

  return dao.saveCollection(collection)
}, (db) => {
  const dao = new Dao(db)
  const collection = dao.findCollectionByNameOrId("xz7ejtfibmeoyom")

  collection.indexes = []

  return dao.saveCollection(collection)
})
