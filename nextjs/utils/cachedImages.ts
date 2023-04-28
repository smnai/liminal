import cloudinary from './cloudinary'

let cachedResults

export default async function getResults() {
  if (!cachedResults) {
    const fetchedResults = await cloudinary.v2.search
      .expression(`folder:${process.env.CLOUDINARY_FOLDER}/*`)
      .max_results(500)
      .execute()

    cachedResults = fetchedResults
  }

  return cachedResults
}
