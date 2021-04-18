export interface Country {
  name: string;
}

export interface City {
  name: string;
  country: Country;
}

export interface Location {
  city: City;
  name: string;
  address_1: string;
  address_2: string;
  longitude: number;
  latitude: number;
}

export interface GroupUrlname {
  urlname: string;
}

export interface MeetupGroup {
  id: number;
  name: string;
  description: string;
  status: string;
  link: string;
  photo_link: string;
  member_count: number;
  location: Location;
  urlname: GroupUrlname;
}
