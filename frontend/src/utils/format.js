import { format } from 'date-fns';

export const formatLocalDate = (date: string, pattern: string) => {
    const dt = new Date(date);
    const dtDateOnly = new Date(dt.valueOf() + dt.getTimezoneOffset() * 60 * 1000);
    return format(dtDateOnly, pattern);
}

export const formatDateToDatePicker = (date:string) => {
  const dt = new Date(date);
  return dt.toISOString().split('T')[0];
}
