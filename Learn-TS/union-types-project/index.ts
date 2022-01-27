import courses from './courses'
import studyGroups from './studyGroups'


type Course = {
  id: number,
  studyGroup: number,
  title: string,
  keywords: string[],
  eventType: string
}

type StudyGroup = {
  id: number,
  courseId: number,
  title: string,
  keywords: string[],
  eventType: string
}

type SearchEventOptions = {
  query: number | string,
  eventType: 'courses' | 'groups'
}

function searchEvents(options: SearchEventOptions) {
  let events: (Course | StudyGroup)[] = studyGroups
  if (options.eventType === 'courses') {
    let events = courses
  }
  return events.filter( (e: Course | StudyGroup) => {
    if(typeof options.query === 'number') {
      if(options.query === e.id) {
        return true
      }
    }
    if(typeof options.query === 'string') {
      return e.keywords.includes(options.query)
    }
  })
}
let enrolledEvents: (Course | StudyGroup)[] = []
function enroll(event: Course | StudyGroup ) {
  enrolledEvents = [...enrolledEvents, event]
}


let searchResults = searchEvents({query: 'art', eventType: 'courses'})
//console.log(searchResults)
enroll(searchResults[0])
console.log(enrolledEvents)
