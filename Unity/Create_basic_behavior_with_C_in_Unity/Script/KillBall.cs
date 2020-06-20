using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class KillBall : MonoBehaviour
{
	public int health;

	private void OnMouseDown()
	{
		health = health -2;

		if (health <=0 )
		{
			Die();
		}
	}
	
	void Die()
	{
		Destroy(gameObject);
	}

}
