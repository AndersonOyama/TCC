package fuzzyLogic;

public class Text {

	private String tittle;
	private float perc_grammatical_error;
	private float share_request;
	private float sensationalist_text;
	
	
	public String getTittle() {
		return tittle;
	}
	public void setTittle(String tittle) {
		this.tittle = tittle;
	}
	public float getPerc_grammatical_error() {
		return perc_grammatical_error;
	}
	public void setPerc_grammatical_error(float perc_grammatical_error) {
		this.perc_grammatical_error = perc_grammatical_error;
	}
	public float getShare_request() {
		return share_request;
	}
	public void setShare_request(float share_request) {
		this.share_request = share_request;
	}
	public float getSensationalist_text() {
		return sensationalist_text;
	}
	public void setSensationalist_text(float sensationalist_text) {
		this.sensationalist_text = sensationalist_text;
	}
	
	public Text(String tit, float perc_error, float share, float sensa) {
		tittle = tit;
		perc_grammatical_error = perc_error;
		share_request = share;
		sensationalist_text = sensa;
	}

	
	
}
