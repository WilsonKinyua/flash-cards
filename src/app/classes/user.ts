export class User {
  constructor(
    public email: string,
    public username: string,
    public first_name: string,
    public last_name: string,
    public date_jioned: Date
  ) // public password: string,
  // public id?: number
  {}
}
